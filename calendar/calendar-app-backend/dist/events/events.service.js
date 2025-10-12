"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.EventsService = void 0;
const common_1 = require("@nestjs/common");
const uuid_1 = require("uuid");
let EventsService = class EventsService {
    constructor() {
        this.events = [];
    }
    createEvent(eventData) {
        const newEvent = { id: (0, uuid_1.v4)(), ...eventData };
        this.events.push(newEvent);
        return newEvent;
    }
    getAllEvents() {
        return this.events;
    }
    getEvent(id) {
        return this.events.find(event => event.id === id);
    }
    updateEvent(id, updatedData) {
        const eventIndex = this.events.findIndex(event => event.id === id);
        if (eventIndex > -1) {
            this.events[eventIndex] = { ...this.events[eventIndex], ...updatedData };
            return this.events[eventIndex];
        }
        return null;
    }
    deleteEvent(id) {
        const eventIndex = this.events.findIndex(event => event.id === id);
        if (eventIndex > -1) {
            return this.events.splice(eventIndex, 1);
        }
        return null;
    }
};
exports.EventsService = EventsService;
exports.EventsService = EventsService = __decorate([
    (0, common_1.Injectable)()
], EventsService);
//# sourceMappingURL=events.service.js.map