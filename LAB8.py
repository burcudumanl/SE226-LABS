class ArchiveItem:
    def __init__(self,uid,title,year):
        self.uid = uid
        self.title = title
        self.year = year
    def __str__(self):
        print("uid:",self.uid)
        print("title:",self.title)
        print("year:",self.year)
    def __eq__(self,other):
        return isinstance(other,ArchiveItem) and self.uid == other.uid
    def is_recent(self,n):
        currentYear=2025
        if(self.year>=currentYear-n):
            return True
class Book(ArchiveItem):
    def __init__(self,uid,title,year,author,pages):
        ArchiveItem.__init__(self,uid,title,year)
        self.author=author
        self.pages=pages
    def __str__(self):
        return f"Book,{self.uid},{self.title},{self.year},{self.author},{self.pages}\n"
class Article(ArchiveItem):
    def __init__(self,uid,title,year,journal,doi):
        ArchiveItem.__init__(self,uid,title,year)
        self.journal=journal
        self.doi=doi
    def __str__(self):
        return f"Article,{self.uid},{self.title},{self.year},{self.journal},{self.doi}\n"
class Podcast(ArchiveItem):
    def __init__(self,uid,title,year,host,duration):
        ArchiveItem.__init__(self,uid,title,year)
        self.host=host
        self.duration=duration
    def __str__(self):
        return f"Podcast,{self.uid},{self.title},{self.year},{self.host},{self.duration}\n"
def save_to_file(items,filename):
    with open(filename,'w') as file:
        for item in items:
            if isinstance(item, Book):
                file.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                file.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                file.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")

def load_from_file(filename):
    items = []
    with open(filename,'r') as file:
        for line in file:
            parts= line.strip().split(',')
            type=parts[0]
            if(type=='Book'):
                items.append(Book(parts[1],parts[2],int(parts[3]),parts[4],int(parts[5])))
            elif(type=='Article'):
                items.append(Article(parts[1],parts[2],int(parts[3]),parts[4],parts[5]))
            elif(type=='Podcast'):
                items.append(Podcast(parts[1],parts[2],int(parts[3]),parts[4],int(parts[5])))
        return items
archive_items=[
    Book("B001", "The Cat Who Loved Sunsets", 2023, "Luna Whiskers", 132),
    Book("B002", "Tea Leaves & Destiny", 2020, "Evelyn Sage", 298),
    Article("A001", "The Psychology of Cloud Watching", 2021, "Daydream Quarterly", "10.1234/fluff.2021.001"),
    Article("A002", "Why Pancakes Are Superior to Waffles", 2019, "Breakfast Journal", "10.456/yum.2019.042"),
    Podcast("P001", "Stargazing With Strangers", 2024, "Nova Night", 55),
    Podcast("P002", "Whale Songs & Ocean Secrets", 2022, "Captain Blue", 48)
    ]
save_to_file(archive_items,"archiveItem.txt")
loaded_items=load_from_file("archiveItem.txt")
print("\n--- Loaded Archive Items ---")
for item in loaded_items:
    print(item)
print("\n--- Items from the Last 5 Years ---")
for item in loaded_items:
    if(item.is_recent(5)):
        print(item)
print("\n--- Articles with DOI starting with '10.123' ---")
for item in loaded_items:
    if(isinstance(item,Article) and item.doi.startswith("10.1234")):
        print(item)





