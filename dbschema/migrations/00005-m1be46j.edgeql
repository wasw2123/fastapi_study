CREATE MIGRATION m1be46j3wx4zihom3zov5zcvkjlxwfmibvg5wx57dyg7yjq7b6c54q
    ONTO m16z4smttjhab7xwspny4kctehn2oysqx4cq4ocj6ytn57rjktnrkq
{
  ALTER TYPE default::Auditable {
      ALTER PROPERTY create_at {
          RENAME TO created_at;
      };
  };
};
