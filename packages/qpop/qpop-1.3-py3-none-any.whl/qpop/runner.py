import os, argparse, time
from inputimeout import inputimeout, TimeoutOccurred

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-g', "--gpus", type=str, required=True, help="The gpu id(s) to run, separated by comma.")
    parser.add_argument('-q', "--queue", type=str, required=True, help="The queue file to read tasks from.")
    args = parser.parse_args()
    
    while True:
        with open(args.queue, 'r') as f:
            lines = f.readlines()
    
        lines_to_write = []
        line_to_run = None
        for line in lines:
            if line_to_run is None and not line.startswith('#'):
                line_to_run = line
                line = f'# {line}'
            lines_to_write.append(line)

        with open(args.queue, 'w') as f:
            f.writelines(lines_to_write)

        if line_to_run is None:
            print('no runs found, waiting for 10 seconds...')
            time.sleep(10)
        else:
            print(f'running: {line_to_run}')
            os.system(f'CUDA_VISIBLE_DEVICES={args.gpus} {line_to_run}')

            try:
                interrupt = inputimeout(timeout=1)
            except TimeoutOccurred:
                interrupt = ''

            if interrupt.lower().strip() in ['end', 'quit', 'q', 'exit']:
                print('interrupted by user, exiting...')
                break
