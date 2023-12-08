using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
 
class Program
{
    static void Main(string[] args)
    {
        List<ScriptureManager> managers = LoadScriptures("scripture.txt");
 
        Console.WriteLine("Welcome to the Scripture Memorizer!");
        Console.WriteLine("Press Enter to hide words, or type 'quit' to exit.");
 
        foreach (var manager in managers)
        {
            Console.ReadLine();
 
            while (!manager.AllWordsHidden)
            {
                Console.Clear();
                manager.HideRandomWords();
                Console.WriteLine(manager.GetVisibleScripture());
                string input = Console.ReadLine().ToLower();
 
                if (input == "quit")
                    return; // exit the program
            }
 
            Console.WriteLine($"Reference: {manager.GetReference()} - All words are hidden. Memorization complete!");
        }
    }
 
    static List<ScriptureManager> LoadScriptures(string filePath)
    {
        List<ScriptureManager> managers = new List<ScriptureManager>();
        string[] scriptureTexts = File.ReadAllLines(filePath);
 
        foreach (var scriptureText in scriptureTexts)
        {
            ScriptureManager manager = new ScriptureManager();
            manager.LoadScripture(scriptureText);
            managers.Add(manager);
        }
 
        return managers;
    }
}
 
class ScriptureManager
{
    private Scripture scripture;
    private List<string> visibleWords;
 
    public bool AllWordsHidden => visibleWords.Count == 0;
 
    public void LoadScripture(string scriptureText)
    {
        scripture = new Scripture(scriptureText);
        visibleWords = new List<string>(scripture.GetWords());
    }
 
    public void HideRandomWords()
    {
        if (!AllWordsHidden)
        {
            int numWordsToHide = Math.Min(3, visibleWords.Count);
            Random random = new Random();
 
            for (int i = 0; i < numWordsToHide; i++)
            {
                int index = random.Next(0, visibleWords.Count);
                visibleWords[index] = "______";
            }
        }
    }
 
    public string GetReference()
    {
        return scripture.GetReference();
    }
 
    public string GetVisibleScripture()
    {
        return $"{GetReference()} - {string.Join(" ", visibleWords)}";
    }
}
 
class Scripture
{
    private string reference;
    private string text;
    private string[] words;
 
    public Scripture(string fullText)
    {
        int referenceEnd = fullText.IndexOf(' ');
        reference = fullText.Substring(0, referenceEnd).Trim();
        text = fullText.Substring(referenceEnd).Trim();
        words = text.Split(' ');
    }
 
    public string GetReference()
    {
        return reference;
    }
 
    public string GetText()
    {
        return text;
    }
 
    public string[] GetWords()
    {
        return words;
    }
}