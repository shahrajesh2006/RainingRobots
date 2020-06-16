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
    session_attr['guess_number'] = random.randint(0, 100)#Generate the random number and store in the session
    session_attr['no_of_guesses'] = 0

    speech_text = (
        "Welcome to the High Low guessing game created by RR Game. Say a number between 1 and 100")

    handler_input.response_builder.speak(speech_text).ask(speech_text)
    
    return handler_input.response_builder.response

#This is NumberGuessIntent
@sb.request_handler(can_handle_func=lambda input:is_intent_name("NumberGuessIntent")(input))
def number_guess_handler(handler_input):
    """Handler for processing guess with target."""
    # type: (HandlerInput) -> Response
    session_attr = handler_input.attributes_manager.session_attributes
    target_num = session_attr["guess_number"]
    guess_num = int(handler_input.request_envelope.request.intent.slots[
        "number"].value)

    session_attr["no_of_guesses"] = session_attr["no_of_guesses"]+1 #Increment number of guess by 1

    if guess_num > target_num:
        speech_text = (
            "{} is too high. Try saying a smaller number.".format(guess_num))
        reprompt = "Try saying a smaller number."
        handler_input.response_builder.speak(speech_text).ask(reprompt)

    elif guess_num < target_num:
        speech_text = (
            "{} is too low. Try saying a larger number.".format(guess_num))
        reprompt = "Try saying a larger number."
        handler_input.response_builder.speak(speech_text).ask(reprompt)
    elif guess_num == target_num:
        speech_text = (
            "Congratulations. {} is the correct guess. "
            "You guessed the number in {} guesses. "
            "Thanks for playing".format(
                guess_num, session_attr["no_of_guesses"]))
        reprompt = "Thanks for playing"
        handler_input.response_builder.speak(
        speech_text).set_should_end_session(True)
    
    return handler_input.response_builder.response

# Igore everything Below here for now----------------------------------------------------------------









#This help intent
@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    # type: (HandlerInput) -> Response
    speech_text = (
        "I am thinking of a number between zero and one hundred, try to "
        "guess it and I will tell you if you got it or it is higher or "
        "lower")
    reprompt = "Try saying a number."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response

#This intent will be for Cancel or Stop
@sb.request_handler(
    can_handle_func=lambda input:
        is_intent_name("AMAZON.CancelIntent")(input) or
        is_intent_name("AMAZON.StopIntent")(input))
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Thanks for playing!!"

    handler_input.response_builder.speak(
        speech_text).set_should_end_session(True)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # type: (HandlerInput) -> Response
    
    
    return handler_input.response_builder.response




#This is yes intent
@sb.request_handler(can_handle_func=lambda input:is_intent_name("AMAZON.YesIntent")(input))
def yes_handler(handler_input):
    """Handler for Yes Intent, only if the player said yes for
    a new game.
    """
    # type: (HandlerInput) -> Response
    
    speech_text = "Great! Try saying a number to start the game."
    reprompt = "Try saying a number."

    handler_input.response_builder.speak(speech_text).ask(reprompt)
    return handler_input.response_builder.response

#This is no intent
@sb.request_handler(can_handle_func=lambda input:is_intent_name("AMAZON.NoIntent")(input))
def no_handler(handler_input):
    """Handler for No Intent, only if the player said no for
    a new game.
    """
    speech_text = "Ok. See you next time!!"

    handler_input.response_builder.speak(speech_text)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=lambda input:
                    is_intent_name("AMAZON.FallbackIntent")(input))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    # type: (HandlerInput) -> Response
    session_attr = handler_input.attributes_manager.session_attributes

    speech_text ="I did not understand what to do"
    handler_input.response_builder.speak(speech_text).ask(speech_text)
    return handler_input.response_builder.response

#This when the Alexa skill is not able to find a skill based utterance
@sb.request_handler(can_handle_func=lambda input: True)
def unhandled_intent_handler(handler_input):
    """Handler for all other unhandled requests."""
    # type: (HandlerInput) -> Response
    speech = "Say yes to continue or no to end the game!!"
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
