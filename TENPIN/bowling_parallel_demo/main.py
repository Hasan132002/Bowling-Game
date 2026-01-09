from event_source import listen_events
from animation_player import play
from event_map import map_event

print("🎳 Bowling Parallel Animation System")
print("▶ Demo Mode | Hardware Untouched\n")

for event in listen_events():
    mapped = map_event(event)
    print(f"▶ Playing: {mapped}")
    play(mapped)
