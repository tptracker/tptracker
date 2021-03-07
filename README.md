# Which files are important?
tracker

# Inspiration
Ever take a dump and go “Oh SHIT!! I’m out of toilet paper!”? Well, never again (on the CMU campus). As we approach the one year anniversary of the Great Toilet Paper Shortage of 2020, it's easy to remember one thing: Nobody wants to be caught with their pants down-- especially when they're out of toilet paper. Our project plans to upgrade the school system’s hygiene, happiness, and efficiency by notifying custodial staff when and where any toilets are out of toilet paper.

# What it does
Our product detects when toilet paper has run low in a bathroom and notifies custodial staff through an email system.

# How we built it
Using Arduino and python, a list of toilets that are out of toilet paper will be emailed right to custodial. Arduino converts real time data on the state of toilet paper while python processes this data and emails a list of toilet paper deficiencies to an designated email address.

# Challenges we ran into
One challenge was ensuring the output from the Arduino matched what we were looking for in Python’s translation of a CSV file. The main problem with this was that different people worked on the part that created the CSV than used the CSV later on, so we had to make sure everyone communicated what they needed to find a result that worked for everyone. Keeping up good communication kept us from getting twisted up in toilet paper and doubling up or forgetting a section of the project.

We are also not a very artistically inclined group and without much experience with website design, we did not have enough time to dedicate towards learning and implementing a website. Instead of the website or app that groups typically gravitate towards for their projects, we implemented an email system to collect and distribute our data to our customers.

Because we were in different locations, multiple working pieces of hardware were necessary. One teammate focused on designing the circuitry and writing code for the Arduino to CSV file section. Meanwhile, another focused on the actual prototype design on Solidworks. This meant both people needed to have a functional circuit for debugging code and the final project. Teamwork is even more essential when working together remotely!

# Accomplishments that we're proud of
This is tangible and extremely applicable to a real world problem. In a time when we all have to be in separate places, we communicated and ensured everybody was on the same page. We all contributed to a vital piece of the puzzle that came together to be our project. When one part of the project had to be modified, we were able to keep everyone in the loop and active in our setbacks and accomplishments.

# What we learned
We learned how to use smtp and other modules in python to automate sending emails. While not completely flushed out, we gained a basic understanding of the concepts of port and ssl. We also learned how to use serial to communicate between Arduino and Python. Soft skill lessons included how teamwork and communication are even more essential when working together remotely. We learned how to create a centralized vision that can be broken down into individual components that play to the strengths of each individual team member.

# What's next for TPTracker
On the programming side: The app/program may be used by a manager who will assign the people under her/him specific set of bathrooms. Then our program can run some prediction algorithm and could potentially send emails to the respective person responsible for a bathroom before the toilet paper runs out. Making the emails look better may also be in the cards. On the hardware side: We would use something like an encoder to track the turns the roll makes for more accurate predictions and less influence on the paper roll. Or maybe a weight sensor to tell exactly how light, or low, the toilet paper roll is. We would also have to upgrade our hardware from big and bulky Arduinos to a smaller microcontroller with most likely wifi capabilities. Combination: a software that detects when the microcontroller has run out of power

# Built With
arduino
python
serial (api)
smtp (api)
ssl (api)
timeapi
typing(api)
