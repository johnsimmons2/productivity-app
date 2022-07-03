CREATE TABLE IF NOT EXISTS public.transactions
(
    amount integer NOT NULL,
    "categoryId" text COLLATE pg_catalog."default" NOT NULL,
    credit bit(1) NOT NULL,
    date date NOT NULL,
    id text COLLATE pg_catalog."default" NOT NULL,
    "userId" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT transactions_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.transactions
    OWNER to padmin;