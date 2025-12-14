# Project Board Setup

Board: https://github.com/users/muhorocode/projects/4/views/2

## How It's Organized

- **Todo** → tasks not started
- **In Progress** → currently working on
- **Code Review** → PR submitted, waiting for review
- **Done** → completed

Custom fields for each task:
- Priority (high/medium/low)
- Area (your focus)
- Team Member (your name)
- Sprint (week 1, 2, or 3)

## Adding Tasks

Two ways:

**Quick:** Click "+ Add item" in Todo column → type title → click to add details

**Full:** Go to Issues → New issue → add to project → assign yourself

After creating, set Priority, Area, Team Member, Sprint on the right side.

## Starter Tasks

### Demestrine - Backend

1. Flask app setup (app init, config, extensions, requirements)
2. Database models (User, Organization, Shift, Attendance + migrations)
3. Auth API (register, login endpoints + JWT tokens)

### James - Geo & Search

1. Haversine calculator (distance between coordinates)
2. Location validation (validate lat/long, geocoding)
3. Shift search API (distance filtering, proximity sort)

### Elijah - Payment

1. M-Pesa API setup (credentials, service file, test connection)
2. Check-in/out system (geofence verification, time tracking)
3. Payment processing (payout calculation, webhook handling)

### Nassur - Frontend UI

1. React setup (init app, Tailwind, router, Axios)
2. Auth pages (login/register forms, AuthContext, validation)
3. Dashboards (volunteer/org dashboards, profiles, pages)

### Ngatia - Frontend Maps

1. Map integration (Google Maps/Leaflet, shift markers)
2. Location picker (geolocation, address autocomplete, current location)
3. Check-in UI (mobile interface, distance display, API connection)

## Workflow

**Start task:**
- Pick from Todo
- Drag to In Progress
- Branch: `git checkout -b feature/task-name`

**Finish task:**
- Push: `git push origin feature/task-name`
- Create PR with `Closes #issue-number`
- Drag to Code Review
- After approval, merge

## Timeline

- Sprint 1 (Dec 12-18): Setup & foundations
- Sprint 2 (Dec 19-25): Main features
- Sprint 3 (Dec 26-Jan 1): Integration & testing
