-- As the user password can only be updated but never read, we will use this to ask the server if a password provided matches the password of the provided user id.

CREATE OR REPLACE FUNCTION compare_passwords(t1 TEXT, t2 TEXT)
RETURNS bool AS 
$$
DECLARE t3 text;
BEGIN
  SELECT 'password' INTO t3 FROM public.users WHERE id = t1;
  IF t3 = t2 THEN
    RETURN true;
  ELSE
    RETURN false;
  END IF;
END;
$$ LANGUAGE plpgsql;

select test('5265ca0d-cdb9-417c-b2bf-6f6da066d026','ea2cf4ef5b33a4f1bbf57a512ad3c662cbaae97819c086ab71e417916b747c60');