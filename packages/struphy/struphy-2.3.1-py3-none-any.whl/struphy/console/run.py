def struphy_run(model,
                inp=None,
                input_abs=None,
                output='sim_1',
                output_abs=None,
                batch=None,
                batch_abs=None,
                runtime=300,
                save_step=1,
                restart=False,
                mpi=1,
                debug=False,
                cprofile=False,):
    """
    Run a Struphy model: prepare arguments, output folder and execute main().

    Parameters
    ----------
    model : str
        The name of the Struphy model.

    inp : str
        The .yml input parameter file relative to <struphy_path>/io/inp.

    input_abs : str
        The absolute path to the .yml input parameter file.

    output : str
        Name of the output folder in <struphy_path>/io/out.

    output_abs : str
        Absolute path to the output folder.

    batch : str
        Name of the batch script for runs on a cluster.

    batch_abs : str
        Absolute path to the batch scripts for runs on a cluster.

    runtime : int
        Maximum runtime of the simulation in minutes. Will complete the time step and exit after this time is reached.

    save_step : int
        How often to save data in hdf5 file, i.e. every "save_step" time step.

    restart : bool
        Wether to restart an existing simulation.

    mpi : int
        Number of MPI processes for runs with "mpirun".

    debug : bool
        Wether to run in Cobra debug mode, see https://docs.mpcdf.mpg.de/doc/computing/cobra-user-guide.html#interactive-debug-runs'.

    cprofile : bool
        Wether to run with Cprofile (slower).
    """

    import subprocess
    import shutil
    import os
    import struphy
    import yaml

    libpath = struphy.__path__[0]

    with open(os.path.join(libpath, 'state.yml')) as f:
        state = yaml.load(f, Loader=yaml.FullLoader)

    i_path = state['i_path']
    o_path = state['o_path']
    b_path = state['b_path']

    # create absolute i/o paths
    if input_abs is None:
        if inp is None:
            default_yml = os.path.join(i_path, f'params_{model}.yml')
            if os.path.isfile(default_yml):
                print('\nRunning with default parameter file ...')
                input_abs = default_yml
            else:
                # load model class
                from struphy.models import fluid, kinetic, hybrid, toy
                objs = [fluid, kinetic, hybrid, toy]
                for obj in objs:
                    try:
                        model_class = getattr(obj, model)
                    except AttributeError:
                        pass

                params = model_class.generate_default_parameter_file()
                exit()
        else:
            input_abs = os.path.join(i_path, inp)

    if output_abs is None:
        output_abs = os.path.join(o_path, output)

    if batch_abs is None:
        if batch is not None:
            batch_abs = os.path.join(b_path, batch)

    # take existing parameter file for restart
    if restart:
        input_abs = os.path.join(output_abs, 'parameters.yml')

    # command parts
    cmd_python = ['python3']
    cmd_main = ['main.py',
                model,
                '-i',
                input_abs,
                '-o',
                output_abs,
                '--runtime',
                str(runtime),
                '-s',
                str(save_step)]
    cmd_cprofile = ['-m',
                    'cProfile',
                    '-o',
                    os.path.join(output_abs, 'profile_tmp'),
                    '-s',
                    'time']

    # run in normal or debug mode
    if batch_abs is None:

        if debug:
            print('\nLaunching main() in Cobra debug mode ...')
            command = ['srun',
                       '-n',
                       str(mpi),
                       '-p',  # interactive commands
                       'interactive',
                       '--time',
                       '119',
                       '--mem',
                       '2000'] + cmd_python + cprofile*cmd_cprofile + cmd_main

        else:
            print('\nLaunching main() in normal mode ...')
            command = ['mpirun',
                       '-n',
                       str(mpi)] + cmd_python + cprofile*cmd_cprofile + cmd_main

        # add restart flag
        if restart:
            command += ['-r']
            
        if cprofile:
            print('\nCprofile turned on.')
        else:
            print('\nCprofile turned off.')

        # run command as subprocess
        print(f"\nRunning the following command:\n{' '.join(command)}")
        subprocess.run(command, check=True, cwd=libpath)

    # run in batch mode
    else:

        # create output folder if it does not exit
        if not os.path.exists(output_abs):
            os.mkdir(output_abs)
            os.mkdir(os.path.join(output_abs, 'data/'))

        # remove sim.out file
        file = os.path.join(output_abs, 'sim.out')
        if os.path.exists(file):
            os.remove(file)
            print('Removed file ' + file)

        # remove sim.err file
        file = os.path.join(output_abs, 'sim.err')
        if os.path.exists(file):
            os.remove(file)
            print('Removed file ' + file)

        # remove old batch script
        file = os.path.join(output_abs, 'batch_script.sh')
        if os.path.exists(file):
            os.remove(file)
            print('Removed file ' + file)

        # remove struphy.out file
        file = os.path.join(output_abs, 'sim.out')
        if os.path.exists(file):
            os.remove(file)
            print('Removed file ' + file)

        # copy batch script to output folder
        batch_abs_new = os.path.join(output_abs, 'batch_script.sh')
        shutil.copy2(batch_abs, batch_abs_new)

        # delete srun command from batch script
        with open(batch_abs_new, 'r') as f:
            lines = f.readlines()
            if 'srun' in lines[-1]:
                lines = lines[:-2]

        # add new srun command
        with open(batch_abs_new, 'w') as f:
            for line in lines:
                f.write(line)
            f.write('# Run command added by Struphy')

            cmd_string = '\nsrun python3 ' + cprofile * \
                ' '.join(cmd_cprofile) + ' ' + libpath + \
                '/' + ' '.join(cmd_main)

            if restart:
                cmd_string += ' -r'

            cmd_string += ' > ' + os.path.join(output_abs, 'struphy.out')

            f.write(cmd_string)

        # submit batch script in output folder
        print('\nLaunching main() in batch mode ...')
        subprocess.run(['sbatch',
                        'batch_script.sh',
                        ],
                       check=True, cwd=output_abs)
