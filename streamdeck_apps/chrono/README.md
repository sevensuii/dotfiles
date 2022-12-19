# CHRONO

This is a simple stopwatch app for the Stream Deck.

It helps me to keep track of the time I spend on a task.

# Table of contents
- [CHRONO](#chrono)
- [Table of contents](#table-of-contents)
  - [Setup](#setup)
  - [DDBB structure](#ddbb-structure)
  - [Usage](#usage)

## Setup

Copy `chrono.db.example` as `chrono.db` and you're good to go.

```bash
cp chrono.db.example chrono.db
```

## DDBB structure

Here is the structure of the database, in case you want to modify it

```sql
CREATE TABLE relojes(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(50) NOT NULL,
    estado VARCHAR(10) NOT NULL,
    transcurrido TIME,
    ultimo_registro TIME,
    descanso TIME,
    trabajo TIME
);

INSERT INTO relojes (nombre,estado,transcurrido,descanso,trabajo,ultimo_registro) VALUES
	 ('pomodoro','P','00:50:00','00:10:00','00:50:00','00:00:00'),
	 ('timer1','A','01:22:21','00:00:00','00:00:00','00:00:00'),
	 ('timer2','P','00:00:00','00:00:00','00:00:00','00:00:00');
```

## Usage

```bash
app.py [type] [number] [option]
```

- `type` can by pomodoro or timer
- `number` is the number of the timer
- `option` can be play-pause, reset, restore

Examples: 

- `app.py timer 1 play-pause` will play/pause the timer 1
- `app.py timer 1 reset` will save current time to `ultimo_registro` and set current time to 0
- `app.py timer 1 restore` will set current time to `ultimo_registro`
