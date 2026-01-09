from event_listener import listen_for_event
from event_logic import process_event
from animation_player import play_animation

print("🎳 Bowling Animation System Started")

for event in listen_for_event():
    print("📡 Event received:", event)

    final_event = process_event(event)
    if final_event:
        print("🎬 Playing animation:", final_event)
        play_animation(final_event)
