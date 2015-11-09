CREATE TABLE lbs2.users
(
  nid serial NOT NULL,
  login character varying(50) NOT NULL,
  password character varying(128),
  name character varying(100),
  locked boolean DEFAULT false,
  created timestamp without time zone DEFAULT now(),
  admin integer DEFAULT 0, -- 0-user, 1-admin
  lastlogin timestamp with time zone,
  lastfailedlogin timestamp with time zone,
  failcount integer DEFAULT 0,
  CONSTRAINT pk_users PRIMARY KEY (nid),
  CONSTRAINT uq_users_id UNIQUE (nid),
  CONSTRAINT uq_users_login UNIQUE (login)
)
WITH (
  OIDS=FALSE
);
CREATE TABLE lbs2.providers
(
  nid serial NOT NULL,
  name character varying,
  CONSTRAINT providers_pkey PRIMARY KEY (nid),
  CONSTRAINT providers_name_key UNIQUE (name)
)
WITH (
  OIDS=FALSE
);
CREATE TABLE lbs2.objects
(
  nid serial NOT NULL,
  name character varying(50),
  valid_from timestamp without time zone NOT NULL DEFAULT now(),
  valid_to timestamp without time zone,
  created_by integer,
  provider_id integer,
  created timestamp with time zone NOT NULL DEFAULT now(),
  nofqueries integer DEFAULT 0,
  nofsqueries integer DEFAULT 0,
  lastquery timestamp with time zone,
  active boolean,
  CONSTRAINT pk_objects PRIMARY KEY (nid),
  CONSTRAINT fk_objects_providers FOREIGN KEY (provider_id)
      REFERENCES lbs2.providers (nid) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT uq_objects_id UNIQUE (nid),
  CONSTRAINT uq_objects_name UNIQUE (name)
  
)
WITH (
  OIDS=FALSE
);
CREATE TABLE lbs2.object2user
(
  user_id integer,
  object_id integer,
  visible boolean,
  CONSTRAINT fk_object2user_objects FOREIGN KEY (object_id)
      REFERENCES lbs2.objects (nid) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE,
  CONSTRAINT fk_object2user_users FOREIGN KEY (user_id)
      REFERENCES lbs2.users (nid) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE,
  CONSTRAINT pk_object2user PRIMARY KEY (user_id, object_id)
  
)
WITH (
  OIDS=FALSE
);

CREATE TABLE lbs2.location
(
  nid serial NOT NULL,
  ts timestamp with time zone NOT NULL DEFAULT now(),
  object_id integer,
  bssid character varying(50),
  longitude numeric(11,6),
  latitude numeric(11,6),
  azimuth numeric(10,2),
  distance numeric(10,2),
  other text,
  CONSTRAINT pk_location PRIMARY KEY (nid),
  CONSTRAINT fk_location_objects FOREIGN KEY (object_id)
      REFERENCES lbs2.objects (nid) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE,
  CONSTRAINT uq_location_id UNIQUE (nid)
)
WITH (
  OIDS=FALSE
);
CREATE TABLE lbs2.settings
(
  nid serial NOT NULL,
  name character varying,
  value character varying,
  description character varying,
  CONSTRAINT settings_pkey PRIMARY KEY (nid)
)
WITH (
  OIDS=FALSE
);