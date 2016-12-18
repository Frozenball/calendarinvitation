class AddSecretToEvents < ActiveRecord::Migration
  def change
    add_column :events, :secret, :string
  end
end
