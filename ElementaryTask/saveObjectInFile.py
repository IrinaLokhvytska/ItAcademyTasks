'''Save objects to file and get them from that'''
import pickle


class SaveObject:
    objects = list()
    file = 'test.txt'

    def add_object(self, object):
        if object:
            self.objects.append(object)

    def __save_objects(self):
        with open(self.file, 'wb') as file:
            pickle.dump(self.objects, file)

    def get_object_from_file(self):
        self.__save_objects()
        with open(self.file, 'rb') as f:
            data = pickle.load(f)
        return data

add_object = True
save_object = SaveObject()
while add_object:
    object = input('Enter the object:', )
    save_object.add_object(object)
    answer = input('Do you want to continue? ').strip().upper()
    if answer == 'Y' or answer == 'YES':
        continue
    else:
        print(save_object.get_object_from_file())
        add_object = False
