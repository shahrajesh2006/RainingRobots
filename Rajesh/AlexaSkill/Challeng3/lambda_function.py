# -*- coding: utf-8 -*-

# This is a High Low Guess game Alexa Skill.
# The skill serves as a simple sample on how to use the
# persistence attributes and persistence adapter features in the SDK.


import random
import logging
import os
import boto3

from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response
from ask_sdk_s3.adapter import S3Adapter

SKILL_NAME = 'RR Game'
bucket_name = os.environ.get('S3_PERSISTENCE_BUCKET')
s3_client = boto3.client('s3', config=boto3.session.Config(signature_version='s3v4',s3={'addressing_style': 'path'}))
s3_adapter = S3Adapter(bucket_name=bucket_name, path_prefix="Media", s3_client=s3_client)
sb = CustomSkillBuilder(persistence_adapter=s3_adapter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


SKILL_NAME = 'RR Game'

#This is to handle the Launch Request or Invocation
@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch.

    Get the persistence attributes, to figure out the game state.
    """
    # type: (HandlerInput) -> Response
    
    session_attr = handler_input.attributes_manager.session_attributes
    session_attr["game_status"] = "waiting_for_player1_name" # next status : waiting_for_player2_name,player_one_playing, player_two_playing, results
    
    speech_text = (
        "Welcome to the High Low guessing game created by RR Game. Two players can play this game. Please say the name of player One")

    handler_input.response_builder.speak(speech_text).ask(speech_text)
    
    return handler_input.response_builder.response

#This is NumberGuessIntent
@sb.request_handler(can_handle_func=lambda input:is_intent_name("NumberGuessIntent")(input))
def number_guess_handler(handler_input):
    
    """Handler for processing guess with target."""
    # type: (HandlerInput) -> Respons
    
    session_attr = handler_input.attributes_manager.session_attributes
   #lets find who is playing player 1 or 2 
    if session_attr["game_status"] =="player_one_playing":
        target_num = session_attr["player1_randomNumber"]
        session_attr["player1_attempts"] = session_attr["player1_attempts"]+1 #Increment number of guess by 1
        playerName=session_attr["player1_playerName"]
        attempts= session_attr["player1_attempts"] 
    elif session_attr["game_status"] =="player_two_playing":
        target_num = session_attr["player2_randomNumber"]
        session_attr["player2_attempts"] = session_attr["player2_attempts"]+1 #Increment number of guess by 1
        playerName=session_attr["player2_playerName"]
        attempts= session_attr["player2_attempts"] 
        
    guess_num = int(handler_input.request_envelope.request.intent.slots[
        "number"].value)
    
    if guess_num > target_num:
        speech_text = (
            "{} is too high. {}! try saying a smaller number.".format(guess_num,playerName))
        reprompt = "Try saying a smaller number."
        handler_input.response_builder.speak(speech_text).ask(reprompt)

    elif guess_num < target_num:
        speech_text = (
            "{} is too low. {}! try saying a larger number.".format(guess_num,playerName))
        reprompt = "Try saying a larger number."
        handler_input.response_builder.speak(speech_text).ask(reprompt)
    elif guess_num == target_num:
        if session_attr["game_status"] =="player_one_playing":
            session_attr["game_status"] ="player_two_playing"
            speech_text = (
            "Congratulations {}!. {} is the correct guess. "
            "You guessed the number in {} guesses. "
            "Now player 2 guess a number between 1 and 100".format(playerName,
                guess_num, attempts))
            reprompt="Player two plays"
        elif session_attr["game_status"] =="player_two_playing":
            session_attr["game_status"] ="results"
            speech_text = (
            "Congratulations {}!. {} is the correct guess. "
            "You guessed the number in {} guesses. "
            "Its time to find out who won. Please say results".format(playerName,
                guess_num, attempts))
            reprompt="Time for results"
        handler_input.response_builder.speak(
        speech_text).ask(reprompt)
        
    return handler_input.response_builder.response
    
    #This is NumberGuessIntent
@sb.request_handler(can_handle_func=lambda input:is_intent_name("PlayerNameIntent")(input))
def number_guess_handler(handler_input):
    """Handler for processing TellMyStatus Intent."""
    # type: (HandlerInput) -> Response
    
    player_name=handler_input.request_envelope.request.intent.slots[
        "player_name"].value
        
    # Now lets create the player1 object
    #New_Player=Player(player_name, 50, 0)
    
    session_attr = handler_input.attributes_manager.session_attributes
    
    if session_attr["game_status"] =="waiting_for_player1_name":#If we don't have player one that means its player one name
        session_attr["player1_playerName"] = player_name #Save player one object in session
        session_attr["player1_randomNumber"] = 50 #Save player one object in session
        session_attr["player1_attempts"] = 0 #Save player one object in session
        session_attr["game_status"] ="waiting_for_player2_name"
        speech_text = ("I got the player one name  {}. Please say the name of player Two".format(player_name))
    elif session_attr["game_status"] =="waiting_for_player2_name":#It is player Two Game
        session_attr["player2_playerName"] = player_name #Save player one object in session
        session_attr["player2_randomNumber"] = 75 #Save player one object in session
        session_attr["player2_attempts"] = 0 #Save player one object in session
        session_attr["game_status"] ="player_one_playing"
        speech_text = ("I got the player two name  {}. We are ready to start the game. Player one are you ready. Guess a number between 1 and 100".format(player_name))
    
    handler_input.response_builder.speak(speech_text).ask(speech_text)
    
    return handler_input.response_builder.response

# Igore everything Below here for now----------------------------------------------------------------


#This when the Alexa skill is not able to find a skill based utterance
@sb.request_handler(can_handle_func=lambda input: True)
def unhandled_intent_handler(handler_input):
    """Handler for all other unhandled requests."""
    # type: (HandlerInput) -> Response
    speech = "I am not sure what to do!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response

#This is when code will throw any error
@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    # type: (HandlerInput, Exception) -> Response
    speech = "Sorry, I can't understand that. Please say again!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response

#The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


@sb.global_response_interceptor()
def log_response(handler_input, response):
    """Response logger."""
    # type: (HandlerInput, Response) -> None
    logger.info("Response: {}".format(response))

lambda_handler = sb.lambda_handler()
