
## Event Handling Framework with EventEmitter

This Python module implements an event handling framework (`EventEmitter`) that supports prioritization (`PriorityEvent`), event filtering, and processing using threading, queues (`queue` module), heap operations (`heapq` module), and logging (`logging` module) capabilities.

## Classes

### EventHandler

Defines an interface for handling events.

### NotificationHandler

Extends `EventHandler` and handles notifications with specific `ID` and `Message` attributes.

### Notification

Represents a notification entity with attributes `ID`, `Message`, and `CreatedAt`.

### PriorityEvent

Represents an event with its associated priority for queueing and processing.

### EventEmitter

Manages event registration, emission, and handling. Features include:

- **Logging:** Enables or disables logging and logs events with their priorities.
- **Event Registration:** Registers listeners and handlers for specific events.
- **Event Emission:** Emits events with context for cancellation and timeout.
- **Event Processing:** Processes events in priority order using heap operations.
- **Event Handling:** Dispatches events to registered handlers.

## Example Usage
main.py
```python
import threading
import time
import queue
import logging
from pyeventhub import EventEmitter, NotificationHandler, Notification

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Example usage
    emitter = EventEmitter(logging=True)

    # Register notification handlers
    handler1 = NotificationHandler(name="EmailHandler")
    handler2 = NotificationHandler(name="SMSHandler")

    emitter.on_event("email_notification", handler1)
    emitter.on_event("sms_notification", handler2)

    # Registering listeners with filters
    def email_filter(data):
        if isinstance(data, Notification):
            return data.ID > 0  # Example filter: process only notifications with ID > 0
        return False

    chEmail = emitter.on("email_notification", email_filter)
    chSMS = emitter.on("sms_notification")

    # Simulate sending notifications with priority
    def send_notifications():
        emitter.emit_with_context(None, "email_notification", Notification(ID=1, Message="New email received", CreatedAt=time.time()), 2)  # Higher priority
        emitter.emit_with_context(None, "sms_notification", Notification(ID=2, Message="You have a new SMS", CreatedAt=time.time()), 1)  # Lower priority

    # Handle notifications asynchronously
    def handle_notifications():
        while True:
            if not chEmail.empty():
                notification = chEmail.get()
                print("Received email notification")
                handler1.handle(notification)
            if not chSMS.empty():
                notification = chSMS.get()
                print("Received SMS notification")
                handler2.handle(notification)

    send_thread = threading.Thread(target=send_notifications)
    handle_thread = threading.Thread(target=handle_notifications)

    send_thread.start()
    handle_thread.start()

    # Allow some time for notifications to be processed
    time.sleep(2)

    # Clean up
    emitter.close()
