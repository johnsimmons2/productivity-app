CREATE TABLE IF NOT EXISTS public.transaction_details
(
    id text COLLATE pg_catalog."default" NOT NULL,
    "transactionId" text COLLATE pg_catalog."default" NOT NULL,
    "categoryId" text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    "detailType" integer NOT NULL,
    detail bytea,
    CONSTRAINT transaction_details_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.transaction_details
    OWNER to padmin;