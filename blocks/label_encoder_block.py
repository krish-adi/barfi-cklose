from barfi import Block
from sklearn import preprocessing

label_encoder_block = Block(name='Label Encoder')
label_encoder_block.add_option(name='display-option', type='display', value='Label Encode of the input data.')
label_encoder_block.add_input(name='Data')
label_encoder_block.add_output(name='Labels')
label_encoder_block.add_output(name='Labeled Data')
def label_encoder_block_func(self):
    data = self.get_interface(name='Data')   
    le = preprocessing.LabelEncoder()
    le.fit(data)    
    self.set_interface(name='Labels', value=le.classes_)
    self.set_interface(name='Labeled Data', value=le.transform(data))
label_encoder_block.add_compute(label_encoder_block_func)