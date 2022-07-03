DO
$do$
BEGIN
    IF EXISTS (
        SELECT FROM pg_catalog.pg_roles
        WHERE  rolname = 'padmin') THEN

        RAISE NOTICE 'Role "padmin" already exists. Skipping.';
    ELSE
        BEGIN   -- nested block
            CREATE ROLE padmin WITH
		        LOGIN
		        SUPERUSER
		        INHERIT
		        CREATEDB
		        CREATEROLE
		        NOREPLICATION
		        ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:Q3HFTnuejJbti5bOza57DQ==$+9D69udqd/E+RHt0C57V/Au0EQwXcjmii/skaIV8KGI=:EPzIdDnJrk3HNNH3um3AyuYWgZ61oloMgAtDs5ocnSg=';
        EXCEPTION
            WHEN duplicate_object THEN
                RAISE NOTICE 'Role "padmin" was just created by a concurrent transaction. Skipping.';
        END;
    END IF;
END
$do$;