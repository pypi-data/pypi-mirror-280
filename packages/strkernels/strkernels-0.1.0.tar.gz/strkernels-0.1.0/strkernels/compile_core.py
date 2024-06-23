
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import subprocess
import os

def compile_extension():
    '''
    Compile C core extension for local tests.
    '''

    # Directory where the C files are located
    source_dir = os.path.join(os.path.dirname(__file__), 'core')
    
    # Automatically find all .c files in the source directory
    c_files = [f for f in os.listdir(source_dir) if f.endswith('.c')]
    
    # Compile C files into .o object files
    for c_file in c_files:
        c_file_path = os.path.join(source_dir, c_file)
        o_file_path = c_file.replace('.c', '.o')
        compile_cmd = [
            'gcc', '-fPIC', '-I', source_dir, '-c', c_file_path, '-o', o_file_path, '-fopenmp', '-Wall'
        ]
        print(f"Compiling {c_file}...")
        subprocess.run(compile_cmd, check=True)
    
    # Generated object files
    o_files = [c_file.replace('.c', '.o') for c_file in c_files]
    
    # Output .so file name
    output_file = os.path.join(os.path.dirname(__file__), 'libcore.so')
    
    # Command to link object files into a shared library
    link_cmd = ['gcc', '-shared', '-o', output_file] + o_files + ['-fopenmp', '-Wall']
    
    print("Linking object files...")
    subprocess.run(link_cmd, check=True)
    
    # Clean up .o object files
    for o_file in o_files:
        os.remove(o_file)
    
    print("Compilation completed successfully!")

if __name__ == '__main__':
    compile_extension()
