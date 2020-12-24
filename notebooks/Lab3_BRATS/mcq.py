# MCQ - https://github.com/jupyter-widgets/ipywidgets/issues/2487
# https://levelup.gitconnected.com/deploy-simple-and-instant-online-quizzes-with-jupyter-notebook-tools-5e10f37da531

# See also: Practical AI : Automatically Generate Multiple Choice Questions (MCQs) from any content with BERT Summarizer, Wordnet and Conceptnet
# in https://towardsdatascience.com/practical-ai-automatically-generate-multiple-choice-questions-mcqs-from-any-content-with-bert-2140d53a9bf5

## Basic mcq

#import ipywidgets as widgets
from ipywidgets import widgets, Layout, Box, GridspecLayout
import sys
from IPython.display import display
from IPython.display import clear_output

def create_multipleChoice_widget(description, options, correct_answer, hint):
    if correct_answer not in options:
        options.append(correct_answer)

    correct_answer_index = options.index(correct_answer)

    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False,
        indent = False,
        align = 'center',
    )

    description_out = widgets.Output(layout=Layout(width='auto'))

    with description_out:
        print(description)

    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "correct" + '\x1b[0m' +"\n"
        else:
            s = '\x1b[5;30;41m' + "try again" + '\x1b[0m' +"\n"
        with feedback_out:
            feedback_out.clear_output()
            print(s)
        return

    check = widgets.Button(description="check")
    check.on_click(check_selection)

    hint_out = widgets.Output()

    def hint_selection(b):
        with hint_out:
            print(hint)

        with feedback_out:
            feedback_out.clear_output()
            print(hint)

    hintbutton = widgets.Button(description="hint")
    hintbutton.on_click(hint_selection)

    return widgets.VBox([description_out,
                         alternativ,
                         widgets.HBox([hintbutton, check]), feedback_out],
                        layout=Layout(display='flex',
                                     flex_flow='column',
                                     align_items='stretch',
                                     width='auto'))


# MCQ 1


q1 = 'Which channel (pulse sequence) do you find having the overall best contrast-to-noise ratio (CNR)?'
alt1 = ['FLASH', 'DESS', 'FISP', 'PSIF']
cor1 = 'FLASH'
hint1 = 'See: https://en.wikipedia.org/wiki/Contrast-to-noise_ratio & zoom in'
Lab3_Q1 = create_multipleChoice_widget(q1, alt1, cor1, hint1)



# MCQ 2
Lab3_Q2 = create_multipleChoice_widget('Q2. What kind of pet would you like to have?',
                                  ['cat', 'dog', 'mouse', 'fish'],
                                  'dog',
                                  '[hint]: https://en.wikipedia.org/wiki/Pet'
                                 )
