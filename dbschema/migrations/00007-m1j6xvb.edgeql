CREATE MIGRATION m1j6xvbepqxjkfm7wlph433u4f5ktt24lzwhlub2gxemmmu2cbx6nq
    ONTO m1aoacmvdqpbamxogkbrk677bcjcc6pyzkwl6t3v2nsauxi3qhrfxa
{
  CREATE TYPE default::Participant EXTENDING default::Auditable {
      CREATE REQUIRED LINK meeting: default::Meeting;
      CREATE REQUIRED PROPERTY name: std::str;
  };
  ALTER TYPE default::Meeting {
      CREATE MULTI LINK participants := (.<meeting[IS default::Participant]);
  };
  CREATE TYPE default::ParticipantDate EXTENDING default::Auditable {
      CREATE REQUIRED LINK participant: default::Participant {
          ON TARGET DELETE DELETE SOURCE;
      };
      CREATE REQUIRED PROPERTY date: cal::local_date;
      CREATE CONSTRAINT std::exclusive ON ((.date, .participant));
      CREATE REQUIRED PROPERTY enabled: std::bool {
          SET default := true;
      };
      CREATE REQUIRED PROPERTY starred: std::bool {
          SET default := false;
      };
  };
  ALTER TYPE default::Participant {
      CREATE MULTI LINK dates := (.<participant[IS default::ParticipantDate]);
  };
};
