import { ReactNode } from 'react';
import './PageHeader.css';

type PageHeaderProps = {
  title: string;
  subtitle?: string;
  actions?: ReactNode;
};

export const PageHeader = ({ title, subtitle, actions }: PageHeaderProps) => (
  <header className="page-header">
    <div>
      <p className="eyebrow">NewsKoo</p>
      <h1>{title}</h1>
      {subtitle && <p className="subtitle">{subtitle}</p>}
    </div>
    {actions && <div className="header-actions">{actions}</div>}
  </header>
);
