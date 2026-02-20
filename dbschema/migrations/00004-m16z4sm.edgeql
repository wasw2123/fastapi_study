CREATE MIGRATION m16z4smttjhab7xwspny4kctehn2oysqx4cq4ocj6ytn57rjktnrkq
    ONTO m1n5yjleno2et4us6c566q7awclhhqe3emgu55ogt6zykdsw3rl4pq
{
  CREATE ABSTRACT TYPE default::Auditable {
      CREATE REQUIRED PROPERTY create_at: cal::local_datetime {
          SET default := (cal::to_local_datetime(std::datetime_current(), 'Asia/Seoul'));
          SET readonly := true;
      };
  };
  CREATE TYPE default::Meeting EXTENDING default::Auditable {
      CREATE REQUIRED PROPERTY url_code: std::str {
          SET readonly := true;
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
