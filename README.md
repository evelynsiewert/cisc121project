# cisc121project

# Binary Search
I chose binary search because I have a good understanding of how the algorithm works. I think it would be interesting to create a visual representation of it, as it is slightly complicated and I want to challenge myself.

## Demo video/gif/screenshot of test
<img width="917" height="637" alt="screenshot1" src="https://github.com/user-attachments/assets/88e250ae-4754-47fe-ad3d-e1cf9b458a7b" />
<img width="822" height="850" alt="screenshot2" src="https://github.com/user-attachments/assets/49cba7e2-211b-4df4-8036-7f4e9e42fb0f" />
<img width="827" height="416" alt="screenshot3" src="https://github.com/user-attachments/assets/c0877dae-deea-4ffc-905c-4fe81ec92483" />


## Problem Breakdown & Computational Thinking
- Decomposition: Binary search first finds the middle index of the list using floor division on the list’s length. As well, it begins with the lower constraint as the first index of the list and the upper constraint as the final index of the list. Then it checks whether the target is equal to, less than, or greater than the element in the middle index. If it is less than, the upper constraint is reassigned as one less than the middle index. If it is greater than, the lower constraint is reassigned as one more than the middle index. The middle index is now calculated again to be the midpoint between the lower and upper constraint. The program repeats this using a while loop, with the condition that the loop will run as long as the lower constraint is less than the upper constraint. Binary search may use a boolean value to check whether the target has been found to avoid an incorrect index being returned in the case the target is not in the list.
- Pattern Recognition: We can use pattern recognition to tell that binary search has a O(log2n) time complexity because the number of values to search is being repeatedly cut in half in each iteration of the loop. As well, another pattern in binary search is the repeated check of whether or not the target is less/more than the middle index.
- Abstraction: In order to clearly communicate binary search, the program will have to display to the user the mid index in each iteration, and also will need to display to the user whenever the searching portion of the list becomes shorter. We do not need to display logic such as the value of the found boolean. As well, we do not need to show the user how the validity of the inputs are determined, only that they are invalid (if they are, otherwise the program will just run like normal.)
- Algorithmic Thinking/Design: My binary search program will be for integer lists, as usual. The binary search will take a user inputted target (any integer) in a Gradio Number field, and the list being searched can be randomly generated when the user clicks a button. Once there is a target and list inputted, the user can press another button to begin the binary search (call on the function) and the steps (which will be collected throughout the search process) will be displayed in a text box. 

<img width="421" height="653" alt="binary_search_flowchart" src="https://github.com/user-attachments/assets/a28a43ad-a784-45b1-b34a-383bb05072a5" />

## Steps to Run
1. Press the "Create List" button to generate a list of randomized integers (length 15)
2. Enter a target value into the textbox
3. Press the "Begin Binary Search" button to display the steps binary search takes to locate the target

## Author and Acknowledgement
By Evelyn Siewert\
I did not use generative AI on this assignment
