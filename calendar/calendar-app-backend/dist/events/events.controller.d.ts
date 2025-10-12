import { EventsService, Event } from './events.service';
export declare class EventsController {
    private readonly eventsService;
    constructor(eventsService: EventsService);
    createEvent(eventData: any): Event;
    getAllEvents(): Event[];
    getEvent(id: string): Event;
    updateEvent(id: string, eventData: any): Event;
    deleteEvent(id: string): Event[];
}
