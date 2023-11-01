
import json

class Notebook:

    def __init__(self, path: str = 'notes.json'):
        self.note: dict = {}
        self.not_changed = {}
        self.path = path
    
    def get(self, index: int | None = None):
        if index:
            return self.note.get(index)
        return self.note

    def open_file(self):
        try:
            with open(self.path, 'r', encoding='UTF-8') as file:
                self.note = json.load(file)
                self.not_changed = self.note.copy()
            return True
        except:
            return False

    def save_file(self):
        try:
            with open(self.path, 'w', encoding='UTF-8') as file:
                json.dump(self.note, file, ensure_ascii=False, indent=4)
            return True
        except:
            return False

    def search(self, word: str) -> dict[int:dict[str, str]]:
        result = {}
        for index, note in self.note.items():
            if word.lower() in ' '.join(note.values()).lower():
                result[index] = note
        return result

    def check_id(self):
        if self.note:
            return max(list(map(int, self.note))) + 1
        return 1

    def add_note(self, new: dict[str, str]):
        note = {self.check_id(): new}
        self.note.update(note)

    def change_note(self, i: int, new_note: dict[str, str]):
        note = {i: new_note}
        self.delete_note(i)
        self.note.update(note)

    def delete_note(self, i: int):
        deleted = self.note.pop(i)
        return deleted
    
    def check_on_exit(self):
        if self.note == self.not_changed:
            return False
        else: return True