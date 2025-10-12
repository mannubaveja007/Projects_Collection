export interface Event {
    id: string;
    title: string;
    date: string;
    time: string;
    description?: string;
}
export declare class EventsService {
    private events;
    createEvent(eventData: Partial<Event>): Event;
    getAllEvents(): Event[];
    getEvent(id: string): Event;
    updateEvent(id: string, updatedData: Partial<Event>): Event;
    deleteEvent(id: string): Event[];
}
