import gradio as gr
import random

def random_list_generator():
    numbers = []
    # add 15 random integers to the list
    for i in range(15):
        numbers.append(random.randint(0,50))
    # binary search only works on sorted lists
    numbers = sorted(numbers)
    # convert to string for displaying the list
    num_string = str(numbers)
    return num_string, numbers


def binary_search(nums, target):
    # assign necessary variables
    lower = 0
    upper = len(nums) - 1 # - 1 due to zero indexing
    found = False
    steps = [] # will hold the binary search steps for display
    
    try:
        # check if input is a number
        target = int(target)
    except TypeError:
        steps = ["Please enter a valid target value (Integer)"]

        # ensure all boxes are filled and will not result in error
        while len(steps) < 10: 
            steps.append("")
        return steps

    # check if there are values in the list
    if not nums:
        steps = ["Press the button to create a list before searching!"]

        # ensure all boxes are filled and will not result in error
        while len(steps) < 10: 
            steps.append("")
        return steps

    steps.append(f"Searching list: {nums}") # for clarity
    
    # loop will run until the upper and lower bounds
    while upper >= lower:
        mid = (upper + lower) // 2 # round down in case of an odd length
        steps.append(f"Middle Index: {mid}") # display midpoint
        # check if target has been found
        if nums[mid] == target:
            found = True
            # display result
            steps.append(f"Target {target} has been found at index {mid}")
            break # exit loop
        if nums[mid] < target:
            # begin checking greater half of the list
            lower = mid + 1
            # display this to the user, including the part of the list being searched
            steps.append(f"Now searching right half: {nums[(mid+1):(upper+1)]}")
        else:
            # begin checking smaller half of the list
            upper = mid - 1
            steps.append(f"Now searching left half: {nums[lower:mid]}")
    
    if not found:
        steps.append("Target not in list 😢💔")
    
    # worst case number of messages for an array of length 15
    while len(steps) < 10: 
        steps.append("")
    return steps

# gradio app ui
with gr.Blocks(title = "Binary Search Visualization") as demo:
    # on-screen page title + description/instructions
    gr.Markdown("# **Binary Search Visualization** 👀")
    gr.Markdown("Generate a list, input a target and press the button to begin the binary search! 🔥👀")

    # store the list
    store_list = gr.State([])
    
    create_list = gr.Button("Create Random List 🔥")
    
    list_box = gr.Textbox(label = "Random List", interactive = False)
    user_target = gr.Number(label = "Enter a Target", value = 1, interactive = True, precision = None)
    
    create_list.click(
        # list will be generated when clicking this button
        fn = random_list_generator, 
        inputs = [],
        # sends the display string to the list box
        # and the list itself to be stored
        outputs = [list_box, store_list]
    )

    start_search = gr.Button("Begin Binary Search ‼️", variant = 'huggingface')
    
    steps_box = [gr.Textbox(label = f"Step {i+1}", interactive = False) for i in range(10)]
        
    
    start_search.click(
        fn = binary_search,
        # takes the State and user input target as parameters to binary search
        inputs = [store_list, user_target],
        # sends all resulting steps to the steps box for display
        outputs = steps_box
    )

demo.launch()
