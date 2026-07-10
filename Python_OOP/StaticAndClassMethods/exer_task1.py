class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // 4 + (1 if photos_count % 4 != 0 else 0)
        return cls(pages)

    def add_photo(self, label):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"
        return "No more free slots"

    def display(self):
        result = ""
        for page in self.photos:
            result += "-----------\n"
            result += " ".join(["[]" for _ in page]) + "\n"
        result += "-----------\n"
        return result
