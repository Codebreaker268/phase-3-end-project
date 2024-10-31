from database import session
from models import Novel, Chapter,Character,Theme 
def display_menu():
    print("\nBook Writing Planner")
    print("1. Add Novel")
    print("2. List Novels")
    print("3. Add Chapter")
    print("4. List Chapters for a Novel")
    print("5. Exit")

def add_novel():
    title = input("Enter the title of the novel: ")
    genre = input("Enter the genre: ")
    author = input("Enter the author: ")
    status = input("Enter the status: ")

    new_novel = Novel(title=title, genre=genre, author=author, status=status)
    session.add(new_novel)
    session.commit()
    print(f"Novel '{title}' added successfully.")

def list_novels():
    novels = session.query(Novel).all()
    for novel in novels:
        print(f"{novel.id}: {novel.title} by {novel.author} - {novel.status}")

def add_chapter():
    list_novels()  # Show existing novels to select from
    novel_id = int(input("Enter the ID of the novel to add a chapter to: "))
    title = input("Enter the title of the chapter: ")
    number = int(input("Enter the chapter number: "))
    summary = input("Enter a summary of the chapter: ")
    content = input("Enter the chapter content: ")

    new_chapter = Chapter(title=title, number=number, summary=summary, content=content, novel_id=novel_id)
    session.add(new_chapter)
    session.commit()
    print(f"Chapter '{title}' added to novel ID {novel_id} successfully.")

def list_chapters():
    novel_id = int(input("Enter the ID of the novel to view chapters: "))
    chapters = session.query(Chapter).filter_by(novel_id=novel_id).all()
    for chapter in chapters:
        print(f"Chapter {chapter.number}: {chapter.title} - {chapter.summary}")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_novel()
        elif choice == '2':
            list_novels()
        elif choice == '3':
            add_chapter()
        elif choice == '4':
            list_chapters()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
