# DS2002FinalProject

PART 1 DEPLOYMENT/ BENCHMARKS 1-4: All code is in part1.py


PART 1 BENCHMARK 5: Your analysis should look at the relationship between all data fields and their changes over time. In a brief statement, describe any changes or patterns you observe, and propose an explanation for them. Include this in your GitHub repository.

The factor element increases over time in a cubic relationship, starting at 1 at the beginning of the hour, then 8 a minute later, then 27, then 64, and so on, until it reaches 205379/the end of the hour, upon which the factor element resets to 1. Additionally, when the factor element is 1, the pi element is equal to 4.0. Then with each subsequent increase in the factor element, the pi element oscillates between being slightly belowthe true value of pi and slightly above the true value of pi. It alternates in a below-above-below-above pattern. As the factor increases, it gets ever closer to the true value of pi until the factor resets to 1 and the pi element goes back to 4. It may have something to do with whether the factor is an even or an odd number. When the factor is an odd number, the pi element is above true pi. When the factor is an even number, the pi element is below true pi

PART 1 BENCHMARK 6: Screenshot of my pandas database after my code ran for an hour is in Data Retrieval.pdf

PART 1 DOCUMENTATION: I ran a for loop that executed 60 times by running requests.get on the API and appended it to a pandas data frame. To ensure it only ran once every minute, I included a time.sleep(60) statement at the end of the for loop.
