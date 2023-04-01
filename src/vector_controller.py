import anki_vector
from anki_vector.events import Events
from anki_vector.util import degrees
import threading


class TalkAction:
    def __init__(self, message):
        self.message = message


class EmoteAction:
    def __init__(self, angle):
        self.angle = angle


class VectorController:
    def __init__(self):
        self.vector = None
        self._lock = threading.Lock()

    def connect(self):
        with self._lock:
            self.vector = anki_vector.AsyncRobot()
            self.vector.connect()

    def disconnect(self):
        with self._lock:
            if self.vector:
                self.vector.disconnect()
                self.vector = None

    async def talk(self, message):
        with self._lock:
            if self.vector:
                await self.vector.behavior.say_text(message)

    async def emote(self, angle):
        with self._lock:
            if self.vector:
                await self.vector.behavior.set_head_angle(degrees(angle))

    async def act(self, action):
        if isinstance(action, TalkAction):
            await self.talk(action.message)
        elif isinstance(action, EmoteAction):
            await self.emote(action.angle)


# Example usage:
async def main():
    controller = VectorController()
    controller.connect()

    talk_action = TalkAction("Hello, I am Vector!")
    emote_action = EmoteAction(45)

    await controller.act(talk_action)
    await controller.act(emote_action)

    controller.disconnect()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
