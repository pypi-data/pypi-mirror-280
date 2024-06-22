
import threading
import queue
import heapq
import logging

# EventHandler defines an interface for handling events.
class EventHandler:
    def handle(self, data):
        raise NotImplementedError

class NotificationHandler(EventHandler):
    def __init__(self, name):
        self.Name = name

    def handle(self, data):
        if isinstance(data, Notification):
            print(f"[{self.Name}] Received notification: ID {data.ID}, Message: {data.Message}")

class Notification:
    def __init__(self, ID, Message, CreatedAt):
        self.ID = ID
        self.Message = Message
        self.CreatedAt = CreatedAt

# PriorityEvent represents an event with its priority.
class PriorityEvent:
    def __init__(self, event, priority, data):
        self.event = event
        self.priority = priority
        self.data = data

    def __lt__(self, other):
        return self.priority < other.priority

# EventEmitter represents an event emitter.
class EventEmitter:
    def __init__(self, logging=False):
        self.listeners = {}
        self.handlers = {}
        self.events = []
        self.mutex = threading.Lock()
        self.logger = None
        self.set_logging(logging)

    # SetLogging enables or disables logging for the EventEmitter.
    def set_logging(self, enable):
        self.logging = enable
        if self.logging:
            self.logger = logging.getLogger("EventEmitter")
            self.logger.setLevel(logging.INFO)
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("[EventEmitter] %(message)s"))
            self.logger.addHandler(handler)
        else:
            self.logger = None

    # NewEventEmitter creates a new instance of EventEmitter.
    @staticmethod
    def new_event_emitter(logging=False):
        return EventEmitter(logging)

    # On registers a listener for the specified event with optional filters.
    def on(self, event, *filters):
        with self.mutex:
            ch = queue.Queue()
            self.listeners[event] = ch

            def filter_data(data):
                if not filters:
                    return True
                for filter_func in filters:
                    if filter_func(data):
                        return True
                return False

            return ch

    # EmitWithContext emits an event with context for cancellation and timeout.
    def emit_with_context(self, ctx, event, data, priority):
        with self.mutex:
            if self.logging:
                self.logger.info(f"Emitting event {event} with priority {priority}")
            heapq.heappush(self.events, PriorityEvent(event, priority, data))

    # ProcessEvents processes events in priority order.
    def process_events(self, ctx):
        while True:
            with self.mutex:
                if not self.events:
                    return
                heapq.heapify(self.events)  # Re-heapify to maintain heap property
                event_to_process = heapq.heappop(self.events)

            if self.logging:
                self.logger.info(f"Processing event {event_to_process.event} with priority {event_to_process.priority}")

            listeners = self.listeners.get(event_to_process.event, [])
            for ch in listeners:
                try:
                    ch.put(event_to_process.data, block=False)
                except queue.Full:
                    pass

            self.dispatch(event_to_process.event, event_to_process.data)

    # OnEvent registers an event handler for the specified event.
    def on_event(self, event, handler):
        with self.mutex:
            self.handlers.setdefault(event, []).append(handler)

    # Off unregisters all listeners and handlers for the specified event.
    def off(self, event):
        with self.mutex:
            if event in self.listeners:
                del self.listeners[event]
            if event in self.handlers:
                del self.handlers[event]

    # Close closes all event channels and clears the listener map.
    def close(self):
        with self.mutex:
            self.listeners.clear()
            self.handlers.clear()

    # Helper function to dispatch events to registered handlers
    def dispatch(self, event, data):
        with self.mutex:
            handlers = self.handlers.get(event, [])
            for handler in handlers:
                handler.handle(data)
