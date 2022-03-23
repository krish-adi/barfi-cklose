from barfi import Block
import csv

select_file_block = Block(name='Select File')
select_file_block.add_option(name='display-option', type='display', value='Select the file to load data.')
select_file_block.add_option(name='select-file', type='select', items=['file_1.csv', 'file_2.csv'], value='file_1')
select_file_block.add_output(name='File Data')
def select_file_block_func(self):
    file_path = self.get_option(name='select-file')   
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    self.set_interface(name='File Data', value=data[0])
select_file_block.add_compute(select_file_block_func)