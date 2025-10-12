import { Controller, Get, Post, Put, Delete, Body, Param } from '@nestjs/common';
import { EventsService,Event  } from './events.service';

@Controller('events')
export class EventsController {
  constructor(private readonly eventsService: EventsService) {}

  @Post()
  createEvent(@Body() eventData: any) {
    return this.eventsService.createEvent(eventData);
  }

  @Get()
  getAllEvents() {
    return this.eventsService.getAllEvents();
  }

  @Get(':id')
  getEvent(@Param('id') id: string) {
    return this.eventsService.getEvent(id);
  }

  @Put(':id')
  updateEvent(@Param('id') id: string, @Body() eventData: any) {
    return this.eventsService.updateEvent(id, eventData);
  }

  @Delete(':id')
  deleteEvent(@Param('id') id: string) {
    return this.eventsService.deleteEvent(id);
  }
}
