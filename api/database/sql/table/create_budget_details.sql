CREATE TABLE IF NOT EXISTS public.budget_details
(
    id text COLLATE pg_catalog."default" NOT NULL,
    "budgetId" text COLLATE pg_catalog."default" NOT NULL,
    "categoryId" text COLLATE pg_catalog."default" NOT NULL,
    amount money NOT NULL,
    description text COLLATE pg_catalog."default",
    "scheduleId" text COLLATE pg_catalog."default",
    CONSTRAINT budget_details_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.budget_details
    OWNER to padmin;