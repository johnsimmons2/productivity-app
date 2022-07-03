CREATE TABLE IF NOT EXISTS public.budgets
(
    id text COLLATE pg_catalog."default" NOT NULL,
    "userId" text COLLATE pg_catalog."default" NOT NULL,
    amount money NOT NULL,
    "scheduleId" text COLLATE pg_catalog."default",
    name text COLLATE pg_catalog."default" NOT NULL,
    adjustments money DEFAULT 0.00,
    CONSTRAINT budgets_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.budgets
    OWNER to padmin;