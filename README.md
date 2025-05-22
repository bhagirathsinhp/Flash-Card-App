# 🇫🇷🧠 French-English Flash Card App

An interactive **French-English flash card app** built using **Python and Tkinter**. This GUI application is designed to help users learn basic French vocabulary through an intuitive flash card interface. Words are shown in French, then flipped after 3 seconds to reveal the English translation.

---

## 📚 How It Works

- The app displays a **French word** for 3 seconds.
- After that, it **flips the card** to reveal the **English translation**.
- You can click ✅ **(right)** if you know the word or ❌ **(wrong)** if you don't.
- Known words are saved and won't appear again in future sessions.
- When all words are learned, the app congratulates you and disables the buttons.

---

## 🗃️ Folder Structure

    Flash-Card-App/
    │
    ├── images/
    │   ├── card_front.png          # Front side of flash card
    │   ├── card_back.png           # Back side of flash card
    │   ├── right.png               # Right button icon
    │   └── wrong.png               # Wrong button icon
    │
    ├── data/
    │   ├── french_words.csv        # Original word list (required)
    │   └── words_to_learn.csv      # Auto-generated, stores words not yet mastered
    │
    ├── flashcard.py                # Main Python script
    └── screenshot.png              # UI Screenshot (optional)

---

## 💾 How to Use

1. Clone the repo:

        git clone https://github.com/bhagirathsinhp/Flash-Card-App.git
        cd Flash-Card-App

2. Make sure the french_words.csv is present in the ./data/ folder.
3. Run the app
4. Use the ✅ and ❌ buttons to interact and track progress.

---

## 🛠️ Technologies Used

- 🐍 Python 3

- 🪟 Tkinter (for GUI)

- 📄 Pandas (for CSV manipulation)

- 🖼️ PhotoImage & Canvas

---

## 
