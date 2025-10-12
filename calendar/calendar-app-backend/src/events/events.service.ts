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
  private events: Event[] = [];

  createEvent(eventData: Partial<Event>) {
    const newEvent = { id: uuidv4(), ...eventData } as Event;
    this.events.push(newEvent);
    return newEvent;
  }

  getAllEvents() {
    return this.events;
  }

  getEvent(id: string) {
    return this.events.find(event => event.id === id);
  }

  updateEvent(id: string, updatedData: Partial<Event>) {
    const eventIndex = this.events.findIndex(event => event.id === id);
    if (eventIndex > -1) {
      this.events[eventIndex] = { ...this.events[eventIndex], ...updatedData };
      return this.events[eventIndex];
    }
    return null;
  }

  deleteEvent(id: string) {
    const eventIndex = this.events.findIndex(event => event.id === id);
    if (eventIndex > -1) {
      return this.events.splice(eventIndex, 1);
    }
    return null;
  }
}
