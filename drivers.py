import json
import pickle
from xml.dom import minidom


class JSONDriver:
    def __init__(self, path: str):
        self._path = path

    def load_data(self):
        with open(self._path, 'r', encoding='utf-8') as data:
            return json.load(data)

    def save_data(self, data):
        with open(self._path, 'w', encoding='utf-8') as file:
            json.dump(data, file)


class BinaryDriver:
    def __init__(self, path: str):
        self._path = path

    def deserialize(self):
        with open(self._path, 'rb') as data:
            return pickle.load(data)

    def serialize(self, data):
        with open(self._path, 'wb') as file:
            pickle.dump(data, file)


class XMLDrive:
    def __init__(self, path: str = 'test.xml'):
        self._doc = minidom.parse(path)

    def get_title(self):
        return self._doc.getElementsByTagName('test')[0].attributes['title'].value

    def get_questions(self, n):
        return f'{self._doc.getElementsByTagName("question")[n].attributes["text"].value}\n' \
               f'{self._doc.getElementsByTagName("question")[n].getElementsByTagName("answer")[0].attributes["text"].value}\n' \
               f'{self._doc.getElementsByTagName("question")[n].getElementsByTagName("answer")[1].attributes["text"].value}\n' \
               f'{self._doc.getElementsByTagName("question")[n].getElementsByTagName("answer")[2].attributes["text"].value}\n'

    def get_answers(self, n):
        return f'{self._doc.getElementsByTagName("question")[n].attributes["answer"].value}'
