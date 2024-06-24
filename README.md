
# Usecases: 
This project can help lots of student by giving them the ability to quiz themself, and automaticly check the answers using AI
it can save alot of time and make studying more fun

# How to set up:
First thing you will need is python 3.12 which you can download from [here ](https://www.python.org/downloads/release/python-3120)
Next step is to open up windows cmd, you can do so by pressing on the folder path, typing "cmd" and pressing enter
Then you have to enter the command "pip install -r requirements.txt" to install the nessecary requirements to run the program
After doing that, you can run the program by entering the phrase "python app.py", make sure port 17432 is not being used by any application
Then open the browser of your choice and enter the URL "http://127.0.0.1:17432".

# How to use
When opening the webui you will be prompted with the list of the available books, you can add more books by configuring quiz.json file
After choosing the desired book the program will give you options about which lessons you want to choose and how many questions
Next, the program will display the questions and you can write your answers in the input box below each question
Lastly The AI will check your answers, you can configure the AI to use gpt3.5 or gpt4, gpt3.5 is less effiecient and might makes mistakes but is faster than gpt4
and you will be display your percentages on the quiz and the correct answer of all questions, additionaly you will be able to see which questions you wrote wrong


# Ideas
We had many ideas to make this project alot better but there were quite alot of limiting factors so you can read the ideas we had to make this project better
but couldn't do so because of these factors (amount of time needed, the cost to implement such thing)

  - Custom commandline, giving the program the ability to launch on a custom port
  - More dynamic website, we could make that happen by simply making the background move slowly, adding curser moving effect, clicking effect etc
  - Faster response time, The currect API we use is free, if we were able to use the direct openai API this could result in a huge diffrence in wait time
  - Ability to generate questions using AI, We could've made it so the AI could read a document file such as a .pdf .txt .docs etc and makes questions from it

With enough time and motivation, we can make this project alot better than it already is

Thats it, I hope you liked what we made :))
