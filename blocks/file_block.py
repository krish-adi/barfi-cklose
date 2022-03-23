from barfi import Block

file_block = Block(name='File Selection')
file_block.add_option(name='display-option', type='display', value='Enter the path of the file to open.')
file_block.add_option(name='file-path-input', type='input')
file_block.add_output(name='File Path')
def file_block_func(self):
    file_path = self.get_option(name='file-path-input')   
    self.set_interface(name='File Path', value=file_path)
file_block.add_compute(file_block_func)