CREATE TABLE IF NOT EXISTS public.users
(
    id text COLLATE pg_catalog."default" NOT NULL,
    "firstName" text COLLATE pg_catalog."default",
    "lastName" text COLLATE pg_catalog."default",
    email text COLLATE pg_catalog."default",
    username text COLLATE pg_catalog."default" NOT NULL,
    password text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT user_email UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to padmin;