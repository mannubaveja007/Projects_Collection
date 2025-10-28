import { Injectable } from '@nestjs/common';
import { v4 as uuidv4 } from 'uuid';

export interface Event {  // Export the Event interface
  id: string;
  title: string;
  date: string;
  time: string;
  description?: string;
}

@Injectable()
export class EventsService {
  private events: Map<string, Event> = new Map();

  createEvent(eventData: Partial<Event>) {
    const newEvent = { id: uuidv4(), ...eventData } as Event;
    this.events.set(newEvent.id, newEvent);
    return newEvent;
  }

  getAllEvents() {
    return Array.from(this.events.values());
  }

  getEvent(id: string) {
    return this.events.get(id);
  }

  updateEvent(id: string, updatedData: Partial<Event>) {
    const event = this.events.get(id);
    if (event) {
      const updatedEvent = { ...event, ...updatedData };
      this.events.set(id, updatedEvent);
      return updatedEvent;
    }
    return null;
  }

  deleteEvent(id: string) {
    const event = this.events.get(id);
    if (event) {
      this.events.delete(id);
      return [event];
    }
    return null;
  }
}
