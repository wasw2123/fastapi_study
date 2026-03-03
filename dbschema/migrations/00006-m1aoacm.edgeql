CREATE MIGRATION m1aoacmvdqpbamxogkbrk677bcjcc6pyzkwl6t3v2nsauxi3qhrfxa
    ONTO m1be46j3wx4zihom3zov5zcvkjlxwfmibvg5wx57dyg7yjq7b6c54q
{
  ALTER TYPE default::Meeting {
      CREATE PROPERTY end_date: cal::local_date;
      CREATE REQUIRED PROPERTY location: std::str {
          SET default := '';
      };
      CREATE PROPERTY start_date: cal::local_date;
      CREATE REQUIRED PROPERTY title: std::str {
          SET default := '';
      };
  };
};
