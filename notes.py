import json
from pathlib import Path

NOTES_FILE = Path("notes.json")

def load_notes() -> list:
    if NOTES_FILE.exists():
        return json.loads(NOTES_FILE.read_text())
    return []

def delete_note(index: int) -> None:
    notes = load_notes()
    if index < 1 or index > len(notes):
        print("No note with that number.")
        return
    removed = notes.pop(index - 1)
    save_notes(notes)
    print(f"Deleted: {removed['text']}")

def save_notes(notes: list) -> None:
    NOTES_FILE.write_text(json.dumps(notes, indent=2))

def add_note(texpyt: str) -> None:
    notes = load_notes()
    notes.append({"text": text})
    save_notes(notes)
    print(f"Added: {text}")

def list_notes() -> None:
    notes = load_notes()
    if not notes:
        print("No notes yet.")
        return
    for i, n in enumerate(notes, start=1):
        print(f"{i}. {n['text']}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 notes.py add \"your note\" | list")
        raise SystemExit(1)
    cmd = sys.argv[1]
    if cmd == "add":
        add_note(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_notes()
    elif cmd == "delete":
        if len(sys.argv) < 3:
            print("Usage: python3 notes.py delete <number>")
            raise SystemExit(1)
        delete_note(int(sys.argv[2]))
    else:
        print("Unknown command. Use add, list, or delete.")