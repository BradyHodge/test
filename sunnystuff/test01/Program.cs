using System;
using System.Collections.Generic;
using System.IO;
 
// Entry class to represent a journal entry
public class Entry
{
    public string Prompt { get; set; }
    public string Response { get; set; }
    public string Date { get; set; }
 
    public Entry(string prompt, string response, string date)
    {
        Prompt = prompt;
        Response = response;
        Date = date;
    }
 
    // Override ToString for easy display
    public override string ToString()
    {
        return $"{Date} - {Prompt}: {Response}";
    }
}
 
// Journal class to manage entries
public class Journal
{
    private List<Entry> entries = new List<Entry>();
 
    // Method to add a new entry
    public void AddEntry(string prompt, string response, string date)
    {
        Entry newEntry = new Entry(prompt, response, date);
        entries.Add(newEntry);
        Console.WriteLine("Entry added successfully!");
    }
 
    // Method to display all entries
    public void DisplayEntries()
    {
        if (entries.Count == 0)
        {
            Console.WriteLine("No entries found.");
        }
        else
        {
            foreach (var entry in entries)
            {
                Console.WriteLine(entry);
            }
        }
    }
 
    // Method to save the journal to a file
    public void SaveToFile(string fileName)
    {
        using (StreamWriter outputFile = new StreamWriter(fileName))
        {
            foreach (var entry in entries)
            {
                outputFile.WriteLine($"{entry.Date},{entry.Prompt},{entry.Response}");
            }
        }
 
        Console.WriteLine("Journal saved to file successfully!");
    }
 
    // Method to load the journal from a file
    public void LoadFromFile(string fileName)
    {
        if (File.Exists(fileName))
        {
            entries.Clear(); // Clear existing entries
 
            string[] lines = File.ReadAllLines(fileName);
            foreach (var line in lines)
            {
                string[] parts = line.Split(",");
                if (parts.Length == 3)
                {
                    string date = parts[0];
                    string prompt = parts[1];
                    string response = parts[2];
 
                    Entry loadedEntry = new Entry(prompt, response, date);
                    entries.Add(loadedEntry);
                }
            }
 
            Console.WriteLine("Journal loaded from file successfully!");
        }
        else
        {
            Console.WriteLine("File not found. No entries loaded.");
        }
    }
}
 
class Program
{
    static void Main()
    {
        Journal journal = new Journal();
 
        while (true)
        {
            Console.WriteLine("\nJournal Program Menu:");
            Console.WriteLine("1. Write a new entry");
            Console.WriteLine("2. Display the journal");
            Console.WriteLine("3. Save the journal to a file");
            Console.WriteLine("4. Load the journal from a file");
            Console.WriteLine("5. Exit");
 
            Console.Write("Enter your choice (1-5): ");
            string choice = Console.ReadLine();
 
            switch (choice)
            {
                case "1":
                    Console.WriteLine("Selecting a random prompt...");
                    string[] prompts = {
                        "Who was the most interesting person I interacted with today?",
                        "What was the best part of my day?",
                        "How did I see the hand of the Lord in my life today?",
                        "What was the strongest emotion I felt today?",
                        "If I had one thing I could do over today, what would it be?"
                    };
                    string randomPrompt = prompts[new Random().Next(prompts.Length)];
                    Console.WriteLine($"Prompt: {randomPrompt}");
                    Console.Write("Enter your response: ");
                    string response = Console.ReadLine();
                    Console.Write("Enter the date (MM/DD/YYYY): ");
                    string date = Console.ReadLine();
                    journal.AddEntry(randomPrompt, response, date);
                    break;
 
                case "2":
                    Console.WriteLine("\nDisplaying Journal Entries:");
                    journal.DisplayEntries();
                    break;
 
                case "3":
                    Console.Write("Enter the file name to save the journal: ");
                    string saveFileName = Console.ReadLine();
                    journal.SaveToFile(saveFileName);
                    break;
 
                case "4":
                    Console.Write("Enter the file name to load the journal: ");
                    string loadFileName = Console.ReadLine();
                    journal.LoadFromFile(loadFileName);
                    break;
 
                case "5":
                    Console.WriteLine("Exiting the program. Goodbye!");
                    return;
 
                default:
                    Console.WriteLine("Invalid choice. Please enter a number between 1 and 5.");
                    break;
            }
        }
    }
}