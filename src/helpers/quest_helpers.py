import pyautogui
import time

from helpers.helpers import click

# Function to handle all of the logic required to turn in a quest
def turn_in_quest():
    quest_line_x, quest_line_y = 300, 285
    
    print('Quest Completed\n')
    
    pyautogui.hotkey('l')
    time.sleep(1.5)
    
    click(quest_line_x, quest_line_y)
    time.sleep(1.5)
    
    turn_in_button = pyautogui.locateOnScreen('images/quest_turn_in_button.png')
    
    if turn_in_button != None:
        turn_in_button_x, turn_in_button_y = pyautogui.center(turn_in_button)
        click(turn_in_button_x, turn_in_button_y)
        time.sleep(2)
        
        pyautogui.hotkey('l')
        time.sleep(2)
        
def accept_quest(quest_number):
    exclamation_mark = pyautogui.locateOnScreen('images/exclamation_mark.png')
    if exclamation_mark != None:
        exclamation_mark_x, exclamation_mark_y = pyautogui.center(exclamation_mark)
        click(exclamation_mark_x, exclamation_mark_y)
        
        time.sleep(2)
        
        quests_button = pyautogui.locateOnScreen('images/quests_button.png')
        if quests_button != None:
            quests_button_x, quests_button_y = pyautogui.center(quests_button)
            click(quests_button_x, quests_button_y)
            time.sleep(2)
            
            click(300, 248 + (37 * quest_number))
            time.sleep(2)
            
            accept_button = pyautogui.locateOnScreen('images/quest_accept_button.png')
            if accept_button != None:
                accept_button_x, accept_button_y = pyautogui.center(accept_button)
                click(accept_button_x, accept_button_y)