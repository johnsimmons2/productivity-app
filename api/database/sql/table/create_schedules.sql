CREATE TABLE IF NOT EXISTS public.schedules
(
    id text COLLATE pg_catalog."default" NOT NULL,
    "startDate" text COLLATE pg_catalog."default",
    "endDate" text COLLATE pg_catalog."default",
    chron text COLLATE pg_catalog."default",
    CONSTRAINT schedules_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.schedules
    OWNER to padmin;