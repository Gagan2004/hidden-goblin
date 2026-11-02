path = r'C:\Users\gagan\.gemini\antigravity\brain\b61ca764-e68d-4d40-8041-a8e5315f6293\side_by_side_comparison_report.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

target = 'Mouse cursor tracking subtly directs eye pupils toward the pointer on desktop.'
addition = '''

6. **100% Authentic Puppy Scroll Companion (`PupJourney.jsx` / `.pup-actor`)**:
   - **Inverse Kinematics & Walking Gaits**: Full mathematical model driving 4-leg phase oscillation (`fn`, `ff`, `bn`, `bf`), body bobbing, tail wagging, ear twitches, eye blinking, and gaze tracking.
   - **Hero Quilt Emergence & Arcing**: Starts behind the quilt with ledge paws resting on the sill (`layerFront="false"`, `ledge="1"`); upon scrolling down, arcs up over the quilt boundary and transitions to the side-walking stance (`layerFront="true"`, `side="1"`).
   - **Cubic Bezier Path & Hold Intervals**: Smoothly interpolates along quintic smootherstep curves between section stops (`[data-pup-stop]`), locking into place at each section.
   - **Interactive Pawprints & Idle Detection**: Drops fading paw print stamps (`.pup-prints`) during scroll motion; pauses into a standing stance when scrolling stops, and pops an idle speech bubble (`"coming?"`) after 2.6s of inactivity.
   - **Click Actions & Gaze**: Clickable companion that hops, woofs, sneezes, or bursts hearts, with gaze dynamically tracking the mouse pointer.'''

if target in text:
    text = text.replace(target, target + addition, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated report successfully!')
else:
    print('Target not found')

