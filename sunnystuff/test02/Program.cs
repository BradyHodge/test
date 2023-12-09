using System;
using System.Threading;
 
// Base class for MindfulnessActivity
public abstract class MindfulnessActivity
{
    protected string name;
    protected string description;
    protected int duration;
 
    public MindfulnessActivity(string name, string description)
    {
        this.name = name;
        this.description = description;
    }
 
    public void Start()
    {
        DisplayStartingMessage();
        PrepareActivity();
        PerformActivity();
        DisplayEndingMessage();
    }
 
    protected void DisplayStartingMessage()
    {
        Console.WriteLine($"*** {name} Activity ***");
        Console.WriteLine(description);
        Console.Write("Enter the duration (in seconds): ");
        duration = int.Parse(Console.ReadLine());
        Console.WriteLine("Get ready to begin...");
        Pause(3);
    }
 
    protected abstract void PrepareActivity();
 
    protected abstract void PerformActivity();
 
    protected void DisplayEndingMessage()
    {
        Console.WriteLine("Great job! You have completed the activity.");
        Console.WriteLine($"You spent {duration} seconds on the {name} activity.");
        Pause(3);
    }
 
    protected void Pause(int seconds)
    {
        for (int i = seconds; i > 0; i--)
        {
            Console.Write($"{i} ");
            Thread.Sleep(1000);
        }
        Console.WriteLine();
    }
}
 
// BreathingActivity class
public class BreathingActivity : MindfulnessActivity
{
    public BreathingActivity() : base("Breathing", "This activity will help you relax by guiding you through deep breathing.")
    {
    }
 
    protected override void PrepareActivity()
    {
        // Additional preparation for breathing activity if needed
    }
 
    protected override void PerformActivity()
    {
        for (int i = 0; i < duration; i++)
        {
            Console.WriteLine("Breathe in...");
            Pause(2);
            Console.WriteLine("Breathe out...");
            Pause(2);
        }
    }
}
 
// ReflectionActivity class
public class ReflectionActivity : MindfulnessActivity
{
    private string[] prompts = {
        "Think of a time when you stood up for someone else.",
        "Think of a time when you did something really difficult.",
        "Think of a time when you helped someone in need.",
        "Think of a time when you did something truly selfless."
    };
 
    private string[] reflectionQuestions = {
        "Why was this experience meaningful to you?",
        "Have you ever done anything like this before?",
        // Add more reflection questions as needed
    };
 
    public ReflectionActivity() : base("Reflection", "This activity will help you reflect on times in your life when you have shown strength and resilience.")
    {
    }
 
    protected override void PrepareActivity()
    {
        // Additional preparation for reflection activity if needed
    }
 
    protected override void PerformActivity()
    {
        Random random = new Random();
 
        for (int i = 0; i < duration; i++)
        {
            string randomPrompt = prompts[random.Next(prompts.Length)];
            Console.WriteLine(randomPrompt);
 
            foreach (var question in reflectionQuestions)
            {
                Console.WriteLine(question);
                Pause(3);
            }
        }
    }
}
 
// ListingActivity class
public class ListingActivity : MindfulnessActivity
{
    private string[] listingPrompts = {
        "Who are people that you appreciate?",
        "What are personal strengths of yours?",
        // Add more listing prompts as needed
    };
 
    public ListingActivity() : base("Listing", "This activity will help you reflect on the good things in your life by having you list as many things as you can in a certain area.")
    {
    }
 
    protected override void PrepareActivity()
    {
        // Additional preparation for listing activity if needed
    }
 
    protected override void PerformActivity()
    {
        Random random = new Random();
        string randomPrompt = listingPrompts[random.Next(listingPrompts.Length)];
 
        Console.WriteLine(randomPrompt);
        Pause(3);
 
        Console.WriteLine("Start listing items...");
 
        DateTime startTime = DateTime.Now;
        DateTime endTime = startTime.AddSeconds(duration);
 
        int itemCount = 0;
        while (DateTime.Now < endTime)
        {
            // Simulate user entering items (you may replace this with actual user input)
            Console.WriteLine("Enter an item: ");
            Console.ReadLine();
            itemCount++;
        }
 
        Console.WriteLine($"You listed {itemCount} items.");
    }
}
 
class Programe
{
    static void Main()
    {
        // Example of using the program
        MindfulnessActivity breathingActivity = new BreathingActivity();
        breathingActivity.Start();
 
        MindfulnessActivity reflectionActivity = new ReflectionActivity();
        reflectionActivity.Start();
 
        MindfulnessActivity listingActivity = new ListingActivity();
        listingActivity.Start();
    }
}
 